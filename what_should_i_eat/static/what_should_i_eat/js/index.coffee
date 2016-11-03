$(document).ready () ->
    console.log "document is ready"

    option_contents = $(".option-contents")
    $(".options").on "click", ".option.more", () ->
        option_contents.slideToggle()
        return true

    $cook_btn = $(".option.yes").closest("a")
    $dismiss_btn = $(".option.no").closest("a")
    tags = $(".choose .tag")
    ingredients = $(".choose .ingredient")
    recipe_overview_url = $("#recipe-overview-url").val()

    tags.add(ingredients).click () ->
        $(@).toggleClass "unselected"
        $.getJSON(
        # $.post(
            recipe_overview_url
            {
                tags: ($(tag).attr("data-id") for tag in tags.filter(":not(.unselected)"))
                ingredients: ($(ingredient).attr("data-id") for ingredient in ingredients.filter(":not(.unselected)"))
            }
            (json) ->
                $(".recipe_overview").replaceWith(json.html)
        )
        return true

    carousel = $(".carousel")
    carousel.slick({
        infinite: true
        slidesToShow: Math.min(3, carousel.find("img").length)
        slidesToScroll: 3
    })
