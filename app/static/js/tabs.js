document.addEventListener('alpine:init', () => {
    Alpine.data('tabs', () => ({
        activeTab: null,
        init() {
            const page = location.href.split('/').at(-1)

            if (!page) return

            switch (page) {
                case '':
                case 'candidates':
                    this.activeTab = 'tab1'
                    break;
                case 'recruiters':
                    this.activeTab = 'tab2'
                    break;
                case 'consultants':
                    this.activeTab = 'tab3'
                    break;
                case 'jobs':
                    this.activeTab = 'tab4'
                    break;
            }
        }
    }))
})