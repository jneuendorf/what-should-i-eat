$(document).ready () ->
    console.log "document is ready"

    option_contents = $(".option-contents")
    $(".options").on "click", ".option.more", () ->
        console.log "her"
        option_contents.slideToggle()

    $(".choose").on "click", ".tag, .ingredient", () ->
        console.log "clicked on tag"
        $tag = $(@)
        $tag.toggleClass "unselected"
        return true

    carousel = $(".carousel")
    carousel.slick({
        infinite: true
        slidesToShow: Math.min(3, carousel.find("img").length)
        slidesToScroll: 3
    })
