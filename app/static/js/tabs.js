document.addEventListener('alpine:init', () => {
    Alpine.data('tabs', () => ({
        tab: null,
        init() {
            const page = location.href.split('/').at(-1).split('?').at(0)

            if (!page) return

            this.tab = page
        },
        isActive(tab) {
            return this.tab === tab
        }
    }))
})