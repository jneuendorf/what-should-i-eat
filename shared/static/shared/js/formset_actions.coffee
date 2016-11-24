# >>> data = {
# ...     'form-TOTAL_FORMS': '1',
# ...     'form-INITIAL_FORMS': '0',
# ...     'form-MAX_NUM_FORMS': '',
# ...     'form-0-title': '',
# ...     'form-0-pub_date': '',
# ... }
# >>> formset = ArticleFormSet(data)
# >>> formset.has_changed()
# False
#
# Understanding the ManagementForm
# You may have noticed the additional data (form-TOTAL_FORMS, form-INITIAL_FORMS and form-MAX_NUM_FORMS) that was required in the formset’s data above. This data is required for the ManagementForm. This form is used by the formset to manage the collection of forms contained in the formset.
# It is used to keep track of how many form instances are being displayed. If you are adding new forms via JavaScript, you should increment the count fields in this form as well. On the other hand, if you are using JavaScript to allow deletion of existing objects, then you need to ensure the ones being removed are properly marked for deletion by including form-#-DELETE in the POST data. It is expected that all forms are present in the POST data regardless.


# "form" in this code is always referring to a form in django form set.
class window.FormSetActions

    @new: (options) ->
        return new @(options)

    constructor: (options) ->
        {
            @prefix
            # Specifies how to find the element to duplicate (from the main input).
            # "form" means a form in django form set.
            @form_container
            # multiple or just 1 more button
            @more_btn_for_each
            @create_more_btn
            @more_btn_container
            @create_less_btn
            @less_btn_container
            @hide_container
        } = $.extend({
            form_container: (input) ->
                return input.parent()
            more_btn_for_each: false
            create_more_btn: () ->
                return $("""<button type="button" class="more">+</button>""")
            create_less_btn: () ->
                return $("""<button type="button" class="less">-</button>""")
            hide_container: (container) ->
                return container.hide(0)
        }, options)

        @total_forms_input = $("[name='#{@prefix}-TOTAL_FORMS']")
        @initial_forms_input = $("[name='#{@prefix}-INITIAL_FORMS']")
        @min_num_forms_input = $("[name='#{@prefix}-MIN_NUM_FORMS']")
        @max_num_forms_input = $("[name='#{@prefix}-MAX_NUM_FORMS']")

        @min_num_forms = parseInt(@min_num_forms_input.val(), 10)
        @max_num_forms = parseInt(@max_num_forms_input.val(), 10)

        @_num_forms = parseInt(@total_forms_input.val(), 10)
        Object.defineProperty(@, "num_forms", {
            get: () ->
                return @_num_forms
            set: (num) ->
                @total_forms_input.val(num)
                @_num_forms = num
                return num
        })

        @_init()

    _init: () ->
        inputs = $("[name^='#{@prefix}']").not("[type='hidden']")
        last_index = inputs.length - 1
        inputs.each (index, element) =>
            input = $(element)
            container = @form_container(input)

            if @more_btn_for_each is true or index is last_index
                @more_btn_container(input).append(@_create_more_btn(input))
            @less_btn_container(input).append(@_create_less_btn(input))
            return true
        return @

    # create buttons for input
    _init_input: (input, {more_btn, less_btn}) ->
        if more_btn is true
            @more_btn_container(input).append(@_create_more_btn(input))
        if less_btn is true
            @less_btn_container(input).append(@_create_less_btn(input))
        return input

    _create_more_btn: (current_input) ->
        return @create_more_btn().addClass("formset_actions").click () =>
            if @num_forms < @max_num_forms
                # TODO: also clone the hidden inputs that hold the model instance id?
                # <input id="id_#{@prefix}-#{index}-id" name="#{@prefix}-#{index}-id" type="hidden" value="#{id}">
                container = @form_container(current_input)
                new_container = @_clone_form(current_input)
                container.after(new_container)
                @num_forms++
            return true

    _create_less_btn: (current_input) ->
        return @create_less_btn().addClass("formset_actions").click () =>
            if @num_forms > @min_num_forms
                current_input.after(@_create_deletion_input(current_input))
                @hide_container(@form_container(current_input))
            return true

    _create_deletion_input: (current_input) ->
        return $("""<input type="hidden" name="#{@prefix}-#{@_index_from_input(current_input)}-DELETE" value="1">""")

    _clone_form: (input) ->
        container = @form_container(input)
        new_container = container.clone()
        form_index = @num_forms
        attrs = ["id", "name", "for"]
        new_container.find("*").each (idx, element) =>
            element = $(element)
            if not element.hasClass("formset_actions")
                for attr in attrs
                    val = element.attr(attr)
                    if val
                        element.attr(attr, @_insert_index_into_attr(val, form_index))
            # remove all elements generated by this class
            # so everything for the new form can be generated again with according data
            else
                element.remove()
        input = new_container.find("[name^='#{@prefix}']").not("[type='hidden']")
        @_init_input(input, {more_btn: @more_btn_for_each, less_btn: true})
        return new_container

    _split_attr: (attr) ->
        return attr.split("-")

    # index as string
    _index_from_input: (input) ->
        return @_split_attr(input.attr("name"))[1]

    # used when cloning a container (-> more button)
    # update e.g. the cloned elements' index in id and name attributes
    _insert_index_into_attr: (attr, index) ->
        parts = @_split_attr(attr)
        return [parts[0], index, parts[2]].join("-")
