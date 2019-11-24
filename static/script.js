// $(document).ready(function () {
//             $('#sidebarCollapse').on('click', function () {
//                 $('#sidebar').toggleClass('active');
//             });
// });


console.log("externer js")

const mySections = document.querySelectorAll('#sidebar');

observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.intersectionRatio > 0) {
            console.log('in the view');
        }  else {
            console.log('out of view. FIRE EVENT!');
        }
    });
});

mySections.forEach(image => {
    observer.observe(image);
});


// document.getElementById('cool').addEventListener('click', function () {
//     console.log('clicked')
// })

// document.querySelector('a#cool').addEventListener('click', function () {
//     console.log('clicked')
// })
  
