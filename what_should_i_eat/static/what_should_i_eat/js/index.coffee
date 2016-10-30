$(document).ready () ->
    console.log "document is ready"

    $(".choose-tags").on "click", ".tag", () ->
        console.log "clicked on tag"
        $tag = $(@)
        $tag.toggleClass "unselected"
        return true

    $(".multiple-items").slick({
        infinite: true
        slidesToShow: 3
        slidesToScroll: 3
    })
