function check(url) {
    const r = confirm("are you sure you want to delete?");
   if (r == true) {
    window.location.href = url;
 }
    
}

$('.carousel').carousel()