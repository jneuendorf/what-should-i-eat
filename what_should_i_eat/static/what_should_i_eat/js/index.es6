$(document).ready(() => {
    const option_contents = $(".option-contents")
    $(".options").on("click", ".option.more", () => {
        option_contents.slideToggle()
    })

    const $cook_btn = $(".option.yes").closest("a")
    const $dismiss_btn = $(".option.no").closest("a")
    const tags = $(".choose .tag")
    const ingredients = $(".choose .ingredient")

    tags.add(ingredients).click(event => {
        $(event.target).toggleClass("unselected")
        $.post(
            django_data.recipe_overview_url,
            {
                tags: tags.filter(":not(.unselected)").toArray().map(tag => $(tag).attr("data-id")),
                ingredients: ingredients.filter(":not(.unselected)").toArray().map(ingredient => $(ingredient).attr("data-id")),
            },
            json => {
                $(".recipe-overview").replaceWith(json.html)
                $('.fotorama').fotorama()
            }
        )
    })
})
