// -*- coding: utf-8 -*-

function check_nonemply(self) {
  let value = self.value
  if (value=="") {
    alert("入力必須項目です")
    self.disabled = true
    return false
  }
  self.disabled = false
  return true
}

const reg_email = /^[\w\.\-]+@[\w\-]+(\.[\w\-]+)*$/
function check_email(self,...submit) {
  let email = self.value
  if (email!="" && ! reg_email.test(email)) {
    alert(email + "はメールアドレスではありません")
    submit.forEach((s)=>{document.getElementById(s).disabled = true})
    return false
  }
  submit.forEach((s)=>{document.getElementById(s).disabled = false})
  return true
}

function check_digit(self) {
  if (! /^\d*$/.test(self.value)) {
    alert('Number is required: '+self.value)
    return false
  }
  return true
}

const reg_stid = /^\d{2}[kK][01]{2}\d{2}$/
function check_studentID(self) {
  let stid = self.value
  if (stid=="") return true
  if (! reg_stid.test(stid)) {
    alert(stid + "は学籍番号ではありません")
    return false
  }
  return true
}

var _entitymap = {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}
function view_html() {
  let html = document.body.innerHTML
  html = html.split(/\n/).slice(2).join('\n')
  console.log(html)
  //let pre = "<pre>" + html.replace(/&<>"'/,(c)=>entitymap[c]||c) + "</pre>"
  //return pre
}
