$(document).ready () ->
    console.log "document is ready"


    # HELPERS
    init_slider = () ->
        carousel = $(".carousel")
        carousel.slick({
            infinite: true
            slidesToShow: Math.min(3, carousel.find("img").length)
            slidesToScroll: 3
        })


    # MAIN
    option_contents = $(".option-contents")
    $(".options").on "click", ".option.more", () ->
        option_contents.slideToggle()
        return true

    $cook_btn = $(".option.yes").closest("a")
    $dismiss_btn = $(".option.no").closest("a")
    tags = $(".choose .tag")
    ingredients = $(".choose .ingredient")

    tags.add(ingredients).click () ->
        $(@).toggleClass "unselected"
        # $.getJSON(
        $.post(
            django_data.recipe_overview_url
            {
                tags: ($(tag).attr("data-id") for tag in tags.filter(":not(.unselected)"))
                ingredients: ($(ingredient).attr("data-id") for ingredient in ingredients.filter(":not(.unselected)"))
            }
            (json) ->
                $(".recipe-overview").replaceWith(json.html)
                init_slider()
                return true
        )
        return true

    init_slider()
