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
    function startTime() {
        const user_date = new Date();
        let h = user_date.getHours();
        let m = user_date.getMinutes();
        h = checkTime(h);
        m = checkTime(m);
        let span_h = document.getElementById('__user_time_hour');
        if (span_h != null) {
            span_h.innerText = h;
        }
        let span_m = document.getElementById('__user_time_mins');
        if (span_m != null) {
            span_m.innerText = m;
        }
        setTimeout(() => {
            startTime();
        }, 1000);
    }
    function checkTime(i) {
        if (i < 10) {
            i = "0" + i;
        }
        ;
        return i;
    }
    function initMapScreen() {
        document.getElementById('logo_div')?.classList.add('animate__fadeOut');
        document.getElementById('wm_on')?.classList.add('opacity-0');
        document.getElementById('logo_div')?.addEventListener('animationend', () => {
            document.getElementById('intro_screen')?.classList.add('hidden');
            document.getElementById('map_screen')?.classList.remove('hidden');
            startTime();
        });
    }
    document.addEventListener('keydown', (ev) => {
        if (ev.key == "Backspace") {
            initMapScreen();
        }
    });
    let formation = 0;
    document.getElementById("logo_div")?.classList.remove('hidden');
    document.getElementById("logo_div")?.classList.add('animate__animated', 'animate__fadeIn');
    setTimeout(() => {
        document.getElementById('logo-char1')?.classList.add('text-[#00773e]');
    }, 1600);
    setTimeout(() => {
        document.getElementById('logo-char2')?.classList.add('text-[#d6c20c]');
    }, 1800);
    setTimeout(() => {
        document.getElementById('logo-char3')?.classList.add('text-[#bc0824]');
        setTimeout(() => {
            document.getElementById('wm_on')?.classList.remove('opacity-0');
        }, 500);
        setTimeout(() => {
            setInterval(() => {
                flashText(document.getElementById('logo-colon'));
            }, 500);
        }, 1000);
        setInterval(() => {
            formation = colorsChange(formation);
        }, 1000);
        setTimeout(() => {
            document.getElementById('logo_text')?.classList.remove('opacity-0', '-mt-[16px]');
        }, 3000);
        setTimeout(() => {
            document.getElementById('logo_text')?.classList.remove('duration-1000');
            setInterval(() => {
                flashText(document.getElementById('logo_text'));
                document.addEventListener('keydown', (e) => {
                    if (e.key == 'Enter') {
                        initMapScreen();
                    }
                });
            }, 500);
        }, 4000);
    }, 2000);
};
