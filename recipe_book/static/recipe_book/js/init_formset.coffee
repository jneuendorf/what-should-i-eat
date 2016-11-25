$(document).ready () ->
    $(".form-group")
        .filter (idx, elem) ->
            return $(elem).find("input[name^='recipe_image']").length > 0
        .formset({
            prefix: "recipe_image"
            addText: "+"
            addCssClass: "btn btn-info add-row"
            deleteText: "-"
            deleteCssClass: "btn btn-danger btn-sm delete-row"
        })
    return true
