const TITLE = "A New Voyage Round the World by William Dampier, 1697 Edition"

const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document)

document.addEventListener('DOMContentLoaded', () => {
    document.title += " | " + TITLE
})