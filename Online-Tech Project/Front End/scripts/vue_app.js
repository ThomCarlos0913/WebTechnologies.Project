// Index page Vue application
var index_vue = new Vue({
  el: "#index-vue",
  data: {
    slideindex: 1,
    slides: null,
    dots: null
  },
  methods: {
    nextslide: function(index) {
      this.showslide(this.slideindex += index)
    },
    gotoslide: function(index) {
      this.showslide(this.slideindex = index)
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
    }
  },
  mounted() {
    this.showslide()
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
      axios.get('http://localhost:5000/validate_account', {
        params: {
          username: this.username,
          password: this.password
        }
      })
      .then(response => {})
    },
    registeraccount: function() {
      if (this.signup_username && this.signup_password && this.signup_confirmpass && this.signup_email){
          if(this.signup_password == this.signup_confirmpass){
            axios.post('http://localhost:5000/register_acount', {
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
    panel_view: null,

    event_name: null,
    event_location: null,
    event_time: null,
    event_details: null,

    update_id: null,
    update_name: null,
    update_location: null,
    update_time: null,
    update_detail: null,

    event_list: null
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
        axios.post('http://localhost:5000/create_event', {
          event_title: this.event_name,
          event_time: this.event_time,
          event_location: this.event_location,
          event_details: this.event_details
        })
        .then(response => {alert("Event created!")})
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
      axios.get('http://localhost:5000/update_event', {
        params: {
          id: this.update_id,
          title: this.update_name,
          venue: this.update_location,
          time: this.update_time,
          details: this.update_detail
        }
      })
    },
    delete_event: function() {
      axios.get('http://localhost:5000/delete_event', {
        params: {
          id: this.update_id
        }
      })
      .then(response => {alert('Event Deleted!')})
    }
  },
  mounted() {
    axios.get('http://localhost:5000/get_events')
    .then(response => {this.event_list = response.data})
  }
});

