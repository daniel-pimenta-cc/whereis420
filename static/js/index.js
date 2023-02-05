"use strict";
//variable that saves the current time when the page is loaded
let initial_time = new Date();
//variable that saves how many minutes have passed since the page was loaded
let minutes_passed = 0;
let original_countdown_value = document.getElementById('countdown_to_420')?.innerHTML;
window.onload = () => {
    //send to countapi.xyz to count the page views
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.countapi.xyz/hit/420blazeit/visits");
    xhr.send();

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
            //arrowMove();
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
    setInterval(() => {
        minutes_passed = updateMinutesPassed(initial_time);
        updateTime();
        setTimeout(() => {}, 100);
        updateCountdown(minutes_passed, original_countdown_value);
        setTimeout(() => {}, 100);
    }, 500);
    //skips the intro screen after 6 seconds by setting initMapScreen to true
    setTimeout(() => {
        initMapScreen(true);
    }, 6000);
};
//function to discover the client timezone 
function getTimezone() {
    return Intl.DateTimeFormat().resolvedOptions().timeZone;
}
console.log(getTimezone());

//funtion that reduce the couwntdown by 1 each minute and update the html
function updateCountdown(minutes_passed,  original_countdown_value) {
    original_countdown_value = parseInt(original_countdown_value);
    minutes_passed = parseInt(minutes_passed);
    let countdown = document.getElementById('countdown_to_420');
    let minutes_element = document.getElementById('current_minute_thing');
    let minutes_int = parseInt(minutes_element.innerHTML);
    let hour_element = document.getElementById('current_hour_thing');
    let hour_int = parseInt(hour_element.innerHTML);
    //if it is btw 16:20 and 16:30 then show the time to blaze it
    if (hour_int == 16 && minutes_int >= 20 && minutes_int <= 30) {
        document.getElementById('countdown_div')?.classList.add('hidden');
        document.getElementById('time_to_blaze')?.classList.remove('hidden');
    }//if it is greater than 16:30 then change the infos to next city and show the countdown
    else if (hour_int == 16 && minutes_int > 29) {
        nextCity();
        document.getElementById('countdown_div')?.classList.remove('hidden');
        document.getElementById('time_to_blaze')?.classList.add('hidden');
    }//else just subtract the minutes passed from the countdown
    else {
        let minutes = original_countdown_value;
        minutes -= minutes_passed;
        countdown.innerHTML = minutes;
    }



    
}
//function that update the html with the current time
function updateTime() {
    let timezone = document.getElementById('timezone_value').innerHTML;
    let minutes_element = document.getElementById('current_minute_thing');
    let minutes_int = parseInt(minutes_element.innerHTML);
    let hour_element = document.getElementById('current_hour_thing');
    let hour_int = parseInt(hour_element.innerHTML);
    let time = new Date();
    //convert the time to the specified timezone
    time = new Date(time.toLocaleString("en-US", { timeZone: timezone }));
    let minutes = time.getMinutes();
    let hours = time.getHours();
    if (minutes_int != minutes) {
        if (minutes < 10) {
            minutes_element.innerHTML = '0' + minutes;
        }
        else
            minutes_element.innerHTML = minutes;
    }
    if (hour_int != hours) {
        if (hours < 10) {
            hour_element.innerHTML = '0' + hours;
        }
        else
            hour_element.innerHTML = hours;
    }


    
}
//function that update the minutes minutes_passed variable by subtracting the current time and the initial_time
function updateMinutesPassed(initial_time) {
    let current_time = new Date();
    let minutes_passed = (current_time - initial_time) / 60000;
    return minutes_passed;
}
//function that change the information for the next city
function nextCity() {
    //get the next city data by makint a request to the /next_city_data endpoint and save to next_data
    let next_data = {};
    let request = new XMLHttpRequest();
    request.open('GET', '/next_city_data', false);
    request.send(null);
    if (request.status === 200) {
        next_data = JSON.parse(request.responseText);
    }

    let text_div = document.getElementById('text_city');
    let desc_div = document.getElementById('text_desc');
    let text_text = next_data.city + ", " + next_data.country;
    let timezone_value = document.getElementById('timezone_value');
    timezone_value.innerHTML = next_data.timezone;
    text_div.innerText = text_text.toUpperCase();
    desc_div.innerText = next_data.desc;
    //replace the subdess by grabbing al the h3 on the info div deleting them and adding the new ones
    let info_div = document.getElementById('info_div');
    let h3s = info_div.getElementsByTagName('h3');
    for (let i = h3s.length - 1; i >= 0; i--) {
        h3s[i].remove();
    }
    let h3s_array = [];
    for (let i = 0; i < next_data.sub_desc.length; i++) {
        let h3 = document.createElement('h3');
        h3.innerText = next_data.sub_desc[i];
        //add the class to the h3
        h3.classList.add('font-pix');
        h3.classList.add('text-[12px]');
        h3.classList.add('my-4');
        h3.classList.add('leading-tight');
        h3.classList.add('mx-2');
        h3.classList.add('md:text-[18px]');

        h3s_array.push(h3);
    }
    //add the new h3s after the h1 with the id text_desc
    let h1 = document.getElementById('text_desc');
    h3s_array.forEach(h3 => h1.after(h3));
    //update the population
    let population = document.getElementById('pop_count_value');
    population.innerText = next_data.pop_count;
    //change the map image
    let map_img = document.getElementById('map_img');
    map_img.src = '../static/images/'+ next_data.map_img;
    //update time
    updateTime();
    //update countdown
    let countdown = document.getElementById('countdown_to_420');
    original_countdown_value = next_data.minutes_to_420;
    countdown.innerHTML = next_data.minutes_to_420;
    initial_time = new Date();
    //hide the time to blaze it
    document.getElementById('countdown_div')?.classList.remove('hidden');
    document.getElementById('time_to_blaze')?.classList.add('hidden');

}