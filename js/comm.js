const TITLE = "A New Voyage Round the World by William Dampier, 1697 Edition"

const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document)

const watchDivPages = (container, onEnter) => {
    const r = /\[p(\d+)\]/i
    const o = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) onEnter(e.target.__pageNumber, e.target)
    }), { root: container })

    const w = document.createTreeWalker(container, NodeFilter.SHOW_TEXT)
    while (w.nextNode()) {
        const m = w.currentNode.nodeValue.match(r)
        if (m) {
            w.currentNode.parentNode.__pageNumber = m[1]
            o.observe(w.currentNode.parentNode)
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.title += " | " + TITLE

    let e = $('#article-pre')
   // e.innerHTML = e.innerHTML.replace(/^ +/gm, '').replace(/^\[.*/gm, m => `<span style="color:#999">${m}</span>`)
   e.innerHTML = e.innerHTML
  .replace(/^ +/gm, '')
  .replace(/^\[img:(.*?) \/\/(.*?)\]/gm, (_, img, cap) => 
    `<figure><img src="../img/illus/${img.trim()}"><figcaption><span style="color:#999">${cap.trim()}</span></figcaption></figure>`
  )
  .replace(/^\[.*/gm, m => `<span style="color:#999">${m}</span>`)

    const scrollDiv = document.querySelector('#con-2cols .right')
    const left = document.querySelector('#con-2cols .left')
    watchDivPages(scrollDiv, (n, element) => {
        console.log("Current page number N:", n)
        const nn = String(n).padStart(4, '0')
        left.innerHTML = `<img src="../p/chapters/${nn}.jpg">`
    })
})