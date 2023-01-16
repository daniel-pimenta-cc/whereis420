"use strict";
window.onload = () => {
    function colorsChange(formation) {
        let return_number = 0;
        if (formation == 0) {
            document.getElementById('logo-char1')?.classList.add('text-[#bc0824]');
            document.getElementById('logo-char2')?.classList.add('text-[#00773e]');
            document.getElementById('logo-char3')?.classList.add('text-[#d6c20c]');
            document.getElementById('logo-char1')?.classList.remove('text-[#00773e]');
            document.getElementById('logo-char2')?.classList.remove('text-[#d6c20c]');
            document.getElementById('logo-char3')?.classList.remove('text-[#bc0824]');
            return_number = formation + 1;
        }
        else if (formation == 1) {
            document.getElementById('logo-char1')?.classList.add('text-[#d6c20c]');
            document.getElementById('logo-char2')?.classList.add('text-[#bc0824]');
            document.getElementById('logo-char3')?.classList.add('text-[#00773e]');
            document.getElementById('logo-char1')?.classList.remove('text-[#bc0824]');
            document.getElementById('logo-char2')?.classList.remove('text-[#00773e]');
            document.getElementById('logo-char3')?.classList.remove('text-[#d6c20c]');
            return_number = formation + 1;
        }
        else if (formation == 2) {
            document.getElementById('logo-char1')?.classList.add('text-[#00773e]');
            document.getElementById('logo-char2')?.classList.add('text-[#d6c20c]');
            document.getElementById('logo-char3')?.classList.add('text-[#bc0824]');
            document.getElementById('logo-char1')?.classList.remove('text-[#d6c20c]');
            document.getElementById('logo-char2')?.classList.remove('text-[#bc0824]');
            document.getElementById('logo-char3')?.classList.remove('text-[#00773e]');
            return_number = 0;
        }
        return return_number;
    }
    function flashText(html_element) {
        if (html_element?.classList.contains('opacity-0')) {
            html_element?.classList.remove('opacity-0');
        }
        else {
            html_element?.classList.add('opacity-0');
        }
    }
    function arrowMove() {
        let arrow_div = document.getElementById('arrow_img');
        arrow_div.classList.contains('mb-8') ? arrow_div.classList.remove('mb-8') : arrow_div.classList.add('mb-8');
        setTimeout(() => {
            arrowMove();
        }, 800);
    }
    function initMapScreen(cheat = true) {
        document.getElementById('logo_div')?.classList.add('animate__fadeOut');
        document.getElementById('wm_on')?.classList.add('opacity-0');
        document.getElementById('logo_div')?.addEventListener('animationend', () => {
            if (cheat) { }
            else {
                clearInterval(6);
                clearInterval(9);
                clearInterval(10);
            }
            document.getElementById('intro_screen')?.classList.add('hidden');
            document.getElementById('map_screen')?.classList.remove('hidden');
            arrowMove();
            document.getElementById('info_div')?.classList.remove('opacity-0');
        });
    }
    document.addEventListener('keydown', (ev) => {
        if (ev.key == "Backspace") {
            initMapScreen(true);
        }
    });
    let formation = 0;
    document.getElementById("logo_div")?.classList.remove('hidden');
    document.getElementById("logo_div")?.classList.add('animate__animated', 'animate__fadeIn');
    setTimeout(() => {
        document.getElementById('logo-char1')?.classList.add('text-[#00773e]');
    }, 1400);
    setTimeout(() => {
        document.getElementById('logo-char2')?.classList.add('text-[#d6c20c]');
    }, 1600);
    setTimeout(() => {
        document.getElementById('logo-char3')?.classList.add('text-[#bc0824]');
        setTimeout(() => {
            document.getElementById('wm_on')?.classList.remove('opacity-0');
        }, 500);
        setTimeout(() => {
            const logo_colon = setInterval(() => {
                flashText(document.getElementById('logo-colon'));
            }, 500);
        }, 800);
        const color_change = setInterval(() => {
            formation = colorsChange(formation);
        }, 800);
        setTimeout(() => {
            document.getElementById('logo_text')?.classList.remove('opacity-0', '-mt-[16px]');
        }, 1500);
        setTimeout(() => {
            document.getElementById('logo_text')?.classList.remove('duration-1000');
            const logo_text_flash = setInterval(() => {
                flashText(document.getElementById('logo_text'));
            }, 500);
            document.addEventListener('keydown', (e) => {
                if (e.key == 'Enter') {
                    initMapScreen();
                }
            });
        }, 3000);
    }, 1700);
};
//function to discover the client timezone 
function getTimezone() {
    return Intl.DateTimeFormat().resolvedOptions().timeZone;
}
console.log(getTimezone());