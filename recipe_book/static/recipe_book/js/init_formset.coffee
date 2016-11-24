$(document).ready () ->
    # formset_actions = new FormSetActions({
    #     prefix: "recipe_image"
    #     # specify how to find the element to duplicate (from the main input)
    #     form_container: (input) ->
    #         return input.closest(".form-group")
    #     create_more_btn: () ->
    #         return $("""<div class="form-group">
    #             <div class="col-sm-2"></div>
    #             <div class="col-sm-10">
    #                 <button type="button" class="btn btn-primary more">+</button>
    #             </div>
    #         </div>""")
    #     more_btn_container: (input) ->
    #         return input.closest("form")
    #     more_btn_for_each: false
    #     create_less_btn: () ->
    #         return $("""<button type="button" class="btn btn-primary less">-</button>""")
    #     less_btn_container: (input) ->
    #         return input.parent()
    #
    # })
    $(".form-group")
        .filter (idx, elem) ->
            return $(elem).find("[name^='recipe_image']").length > 0
        .formset({
            prefix: "recipe_image"
        })
    return true
