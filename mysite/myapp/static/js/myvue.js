var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    }
})

var app2 = new Vue({
    el: '#app-2',
    data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
    }
})

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true
    }
})

var app4 = new Vue({
    el: '#app-4',
    data: { 
        suggestions: [],
        seen:true,
        unseen:false
    },
    created: function() {
        this.fetchSuggestionsList();
        this.timer = setInterval(this.fetchSuggestionsList, 10000);
    },
    methods: { 
        fetchSuggestionsList: function(){
            axios
                .get('/suggestions/')
                //.then(response => console.log(response.data))
                .then(response => (this.suggestions = response.data.suggestions))
            console.log(this.suggestions)
            this.seen=false
            this.unseen=true
        },
        cancelAutoUpdate: function(){clearInterval(this.timer)}
    },
    beforeDestroy(){
        //clearInterval(this.timer)
        this.cancelAutoUpdate();
    }
})  