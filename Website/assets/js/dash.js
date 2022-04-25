function secOnClick(e) {
    $(e.target).addClass("sectionOnCLickToggle");
    Array.from(document.querySelectorAll(".sectionClick")).forEach(function (el) {
      if (e.target !== el) {
        el.classList.remove("sectionOnCLickToggle");
      }
      if(e.target.id==='first'){
          document.getElementsByClassName('second')[0].style.display='none';
          document.getElementsByClassName('third')[0].style.display='none';
          document.getElementsByClassName(e.target.id)[0].style.display='inline' 
      }else if(e.target.id==='second'){
          document.getElementsByClassName('first')[0].style.display='none';
          document.getElementsByClassName('third')[0].style.display='none';
          document.getElementsByClassName(e.target.id)[0].style.display='inline' 
      }else if(e.target.id==='third'){
          document.getElementsByClassName('second')[0].style.display='none';
          document.getElementsByClassName('first')[0].style.display='none';
          document.getElementsByClassName(e.target.id)[0].style.display='inline' 
      }  
    });
    e.target.classList.add("sectionOnCLickToggle");
  }