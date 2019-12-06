function check(id) {
  // Get the checkbox
  var checkBox = document.getElementById("checkbox-"+id);
  var tip = document.getElementById("tips-"+id);
  var form = document.getElementById("form-"+id);
  if (checkBox.checked){
      //change tip to tip-hidden
      tip.classList.add("tip-hidden");
      tip.classList.remove("tips");

      //comment-form en comment-form-hidden

      console.log(form);
      form.classList.remove("comment-form-hidden");
      form.classList.add("comment-form");
  }
  else {
      tip.classList.add("tips");
      tip.classList.remove("tip-hidden");

      form.classList.add("comment-form-hidden");
      form.classList.remove("comment-form");
  }
}