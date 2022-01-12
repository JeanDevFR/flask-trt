document.addEventListener('alpine:init', () => {
    Alpine.data('modal', () => ({
        visible: false,
        message: null,
        next: null,
        open(e) {
            this.message = e.target.dataset.message
            this.next = e.target.dataset.next
            this.visible = true
        },
        close() {
            this.visible = false
            this.message = null
            this.next = null
        },
        submit(e) {
            e.target.action = this.next
            e.target.submit()
        }
    }))
})