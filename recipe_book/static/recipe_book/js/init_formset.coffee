$(document).ready () ->
    formset_actions = new FormSetActions({
        name: "recipe_image"
        # specify how to find the element to duplicate (from the main input)
        form_container: (input) ->
            return input.closest(".form-group")
        create_more_btn: () ->
            return $("""<button type="button" class="btn btn-primary more">+</button>""")
        more_btn_container: (input) ->
            
        more_btn_for_each: false
        create_less_btn: () ->
            return $("""<button type="button" class="btn btn-primary less">-</button>""")
        less_btn_container: (input) ->
            return input.parent()

    })
    return true
