window.onload = () => {
    let formation = 0
    document.getElementById("logo_div").classList.remove('hidden')
    document.getElementById("logo_div").classList.add('animate__animated', 'animate__fadeIn')
    setTimeout(()=>{
        document.getElementById('logo-char1').classList.add('text-[#00773e]');
    }, 1600);
    setTimeout(()=>{
        document.getElementById('logo-char2').classList.add('text-[#d6c20c]');
    }, 1800);
    setTimeout(()=>{
        document.getElementById('logo-char3').classList.add('text-[#bc0824]');
        setInterval(()=> {
            formation = colorsChange(formation)
        }, 1000)
    }, 2000);
    function colorsChange(formation) {
        if (formation == 0) {
            document.getElementById('logo-char1').classList.add('text-[#bc0824]');
            document.getElementById('logo-char2').classList.add('text-[#00773e]');
            document.getElementById('logo-char3').classList.add('text-[#d6c20c]');
            document.getElementById('logo-char1').classList.remove('text-[#00773e]');
            document.getElementById('logo-char2').classList.remove('text-[#d6c20c]');
            document.getElementById('logo-char3').classList.remove('text-[#bc0824]');
            return formation + 1;
        } else if (formation == 1) {
            document.getElementById('logo-char1').classList.add('text-[#d6c20c]');
            document.getElementById('logo-char2').classList.add('text-[#bc0824]');
            document.getElementById('logo-char3').classList.add('text-[#00773e]');
            document.getElementById('logo-char1').classList.remove('text-[#bc0824]');
            document.getElementById('logo-char2').classList.remove('text-[#00773e]');
            document.getElementById('logo-char3').classList.remove('text-[#d6c20c]');
            return formation + 1;
        } else if (formation == 2) {
            document.getElementById('logo-char1').classList.add('text-[#00773e]');
            document.getElementById('logo-char2').classList.add('text-[#d6c20c]');
            document.getElementById('logo-char3').classList.add('text-[#bc0824]');
            document.getElementById('logo-char1').classList.remove('text-[#d6c20c]');
            document.getElementById('logo-char2').classList.remove('text-[#bc0824]');
            document.getElementById('logo-char3').classList.remove('text-[#00773e]');
            return 0;
        }
    }
}

// document.getElementById('world_map').addEventListener('click', (e) => {
//     console.log(e.clientX, e.clientY);
// })