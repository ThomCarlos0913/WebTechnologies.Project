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
    message: "Hello Admin"
  }
});
