// Index page Vue application
var index_vue = new Vue({
  el: "#index-vue",
  data: {
    slideindex: 1,
    slides: null,
    dots: null,
    list_passed: null,
    featured_event: {
      'title':'',
      'venue':'',
      'time':'',
      'details':'',
    },
    t_username: localStorage.getItem('user'),
    t_id: localStorage.getItem('id'),
    t_taken: localStorage.getItem('isTaken'),
    t_privelege: localStorage.getItem('privelege'),
  },
  methods: {
    nextslide: function(index) {
      this.showslide(this.slideindex += index)
    },
    gotoslide: function(index) {
      this.showslide(this.slideindex = index)
    },
    logoutaccount: function() {
      localStorage.clear();
      window.location.href = '../pages/index.html';
    },
    showslide: function(n) {
      // initialization
      this.slides = document.getElementsByClassName("slides");
      this.dots = document.getElementsByClassName("dot");

      if (n > this.slides.length) {
        this.slideindex = 1;
      }
      if (n < 1) {
        this.slideindex = this.slides.length;
      }

      for (var i = 0; i < this.slides.length; i++) {
        this.slides[i].style.display = "none";
      }
      for (var i = 0; i < this.dots.length; i++) {
        this.dots[i].className = this.dots[i].className.replace(" active", "")
      }

      this.slides[this.slideindex - 1].style.display = "block";
      this.dots[this.slideindex - 1].className += " active"
    },
    viewdetails: function(title, venue, time, details) {
      alert('Event Title: ' + title + '\n' +
            'Event Venue: ' + venue + '\n' +
            'Event Time: ' + time + '\n' +
            'Event Details: ' + details + '\n')
    }
  },
  mounted() {
    this.showslide()
    axios.get("/api/get_passed_events")
    .then(response => {this.list_passed = response.data})
    axios.get("/api/get_featured")
    .then(response => {this.featured_event = response.data})
  }
});

// Login page Vue application
var login_vue = new Vue ({
  el: "#login_vue",
  data: {
    username: null,
    password: null,
    show_signup: false,
    signup_username: null,
    signup_password: null,
    signup_confirmpass: null,
    signup_email: null,
    t_username: localStorage.getItem('user'),
    t_id: localStorage.getItem('id'),
    t_taken: localStorage.getItem('isTaken'),
    t_privelege: localStorage.getItem('privelege'),
  },
  methods: {
    displaysignup: function() {
      this.show_signup = true;
    },
    hidesignup: function() {
      this.show_signup = false;
    },
    /* VERIFYACCOUNT FUNCTION NOT YET DONE*/
    verifyaccount: function() {
      axios.get('/api/validate_account', {
        auth: {
          username: this.username,
          password: this.password
        }
      })
      .then(response => {if (response.data['code'] == '200') {
        localStorage.setItem('isTaken', '1')
        localStorage.setItem('user', response.data['user'])
        localStorage.setItem('id', parseInt(response.data['id']))
        localStorage.setItem('privelege', parseInt(response.data['privelege']))
        window.location.href = '../index.html';
      }
    else {
      alert('Username or password is incorrect');
    }})
    },
    registeraccount: function() {
      if (this.signup_username && this.signup_password && this.signup_confirmpass && this.signup_email){
          if(this.signup_password == this.signup_confirmpass){
            axios.post('/api/register_acount', {
                s_user: this.signup_username,
                s_pass: this.signup_password,
                s_email: this.signup_email
            })
            .then(response => {
              if (response.data == "409"){
                alert('ERROR 409: Username already taken by another.')
              }
              else if (response.data == "200") {
                alert('Welcome! Account created.');
                this.show_signup = false;
              }
            })
          }
          else{
            alert('Password and confirm password does not match.')
          }
      }
      else {
        alert('Please fill up all forms')
      }
    }
  }
});

// Admin page Vue Application
var admin_vue = new Vue ({
  el: "#admin_vue",
  data: {
    message: null,
    panel_view: 1,
    event_name: null,
    event_location: null,
    event_time: null,
    event_details: null,
    update_id: null,
    update_name: null,
    update_location: null,
    update_time: null,
    update_detail: null,
    event_list: null,
    t_username: localStorage.getItem('user'),
    t_id: localStorage.getItem('id'),
    t_taken: localStorage.getItem('isTaken'),
    t_privelege: localStorage.getItem('privelege'),
  },
  methods: {
    update_panel: function(panel_number) {
      this.panel_view = panel_number

      switch (panel_number) {
        case 1:
          document.getElementByID("create_btn").className += " admin_btn_active";
          break;
      }
    },
    create_event: function() {
      if (this.event_name && this.event_location && this.event_time && this.event_details) {
        axios.post('/api/create_event', {
          event_title: this.event_name,
          event_time: this.event_time,
          event_location: this.event_location,
          event_details: this.event_details
        })
        .then(response => {alert("Event created!"); document.location.reload(true)})
      }
      else {
        alert("Please fill up all forms")
      }
    },
    get_update_event: function(value, key) {
      this.update_name = value['title']
      this.update_location = value['venue']
      this.update_time = value['time']
      this.update_detail = value['details']
      this.update_id = key
    },
    update_event: function() {
      axios.get('/api/update_event', {
        params: {
          id: this.update_id,
          title: this.update_name,
          venue: this.update_location,
          time: this.update_time,
          details: this.update_detail
        }
      })
      .then(response => {alert('Event Successfully Updated!'); document.location.reload(true)})
    },
    delete_event: function() {
      axios.get('/api/delete_event', {
        params: {
          id: this.update_id
        }
      })
      .then(response => {alert('Event Sucessfully Deleted!'); document.location.reload(true)})
    },
    update_featured: function() {
      axios.get('/api/update_featured', {
        params: {
          id: this.update_id
        }
      })
      .then(response => {alert('Featured Event Updated!'); document.location.reload(true)})
    }
  },
  mounted() {
    axios.get('/api/get_events')
    .then(response => {this.event_list = response.data})
  }
});

// About us page Vue application
var about_page = new Vue({
  el: "#about_vue",
  data: {
    t_username: localStorage.getItem('user'),
    t_id: localStorage.getItem('id'),
    t_taken: localStorage.getItem('isTaken'),
    t_privelege: localStorage.getItem('privelege'),
  },
  methods: {
    logoutaccount: function() {
      localStorage.clear();
      window.location.href = '../pages/index.html';
    }
  }
});

// Event Page Vue application
var event_page = new Vue({
  el: "#events_vue",
  data: {
    event_template: {
      'title': '',
      'venue': '',
      'time': '',
      'details': ''
    },
    event_panel: 1,
    t_username: localStorage.getItem('user'),
    t_id: localStorage.getItem('id'),
    t_taken: localStorage.getItem('isTaken'),
    t_privelege: localStorage.getItem('privelege'),
    test: typeof(parseInt(this.t_id))
  },
  methods: {
    logoutaccount: function() {
      localStorage.clear();
      window.location.href = '../pages/index.html';
    },
    updateeventpanel: function(n) {
      this.event_panel = n;

      if (this.event_panel == 1) {
        axios.get('/api/get_upcoming_event')
        .then(response => {this.event_template = response.data;})
      }
      if (this.event_panel == 2) {
        axios.get('/api/get_my_events', {
          params: {
            user_id: parseInt(this.t_id)
          }
        })
        .then(response => {this.event_template = response.data;})      }
    },
    subscribeevent: function(key, title, time, venue, details) {
      if(this.t_taken) {
        axios.post('/api/subscribe_event', {
          u_id: parseInt(this.t_id),
          e_id: parseInt(key),
          i_title: title,
          i_time: time,
          i_venue: venue,
          i_details: details
        })
        .then(response => {
          if (response.data == "500") {
            alert("ERROR: You are already subscribed here!")
          }
          else if (response.data == "200") {
            alert("Event added to event list!")
          }
        })
      }
      else {
        alert('Please login first before subscribing.')
      }
    },
    unsubscribe: function(key) {
      axios.get("/api/unsubscribe_event", {
          params: {
            event_id: parseInt(key)
          }
      })
      .then(response => {if (response.data == "200") {alert("Sucessfully unsubscribed to event"); document.location.reload(true)}})
    },
    viewdetails: function(title, venue, time, details) {
      alert('Event Title: ' + title + '\n' +
            'Event Venue: ' + venue + '\n' +
            'Event Time: ' + time + '\n' +
            'Event Details: ' + details + '\n')
    }
  },
  mounted() {
    axios.get('/api/get_upcoming_event')
    .then(response => {this.event_template = response.data;})
  }
})
