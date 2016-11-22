class window.FormSetActions

    constructor: (options) ->
        {
            # TODO: maybe use a selector instead?
            @name
            @form_container
            @create_more_btn
            @more_btn_container
            @create_less_btn
            @less_btn_container
        } = $.extend({
            form_container: (input) ->
                return input.parent()
            create_more_btn: () ->
                return $("""<button type="button" class="more">+</button>""")
            create_less_btn: () ->
                return $("""<button type="button" class="less">+</button>""")
        }, options)

        @_init()

    _init: () ->
        inputs = $("[name^='#{@name}']")
        last_index = inputs.length - 1
        inputs.each (index, element) =>
            input = $(element)
            container = @form_container(input)

            if @more_btn_for_each is true or index is last_index
                @more_btn_container(input).append(@create_more_btn())
            @less_btn_container(input).append(@create_less_btn())

            return true



$(document).ready () ->

    return true
