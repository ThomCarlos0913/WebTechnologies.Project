new Vue ({
  el: "#vue-app",
  data: {
    username: null,
    password: null,
    show_signup: false,
    signup_username: null,
    signup_password: null,
    signup_confirmpass: null,
    signup_email: null
  },
  methods: {
    displaysignup: function() {
      this.show_signup = true;
    },
    hidesignup: function() {
      this.show_signup = false;
    }
  }
})
