
window.onload = function () {
    /* Set default height to products images */
    try {
        images = document.getElementsByClassName('products__img')
        let imgHeight = images[0].offsetHeight
        for (let i = 0; i < images.length; i++) {
            images[i].setAttribute('style', `height: ${imgHeight}px;`)
        }
    } catch { }



    /* News Share */
    try {
        vk = document.getElementById('vk')
        ok = document.getElementById('ok')
        twitter = document.getElementById('twitter')
        shareTitle = document.getElementById('social-title').innerHTML
        currentUrl = String(window.location.href).replaceAll('/', '%2F').replace(':', '%3A')
        document.getElementById('social-title').remove()

        var theTop = (screen.height / 2) - 300;
        var theLeft = (screen.width / 2) - 400;
        var features = 'height=600,width=800,top=' + theTop + ',left=' + theLeft + ',toolbar=1,Location=0,Directories=0,Status=0,menubar=1,Scrollbars=1,Resizable=1';

        ok_url = `https://connect.ok.ru/offer?url=${currentUrl}&title=${shareTitle}&utm_source=share2`
        twitter_url = `https://twitter.com/intent/tweet?text=${shareTitle}&url=${currentUrl}&utm_source=share2`
        vk_url = `https://vk.com/share.php?url=${currentUrl}&title=${shareTitle}&utm_source=share2`
        ok.setAttribute('href', ok_url)
        twitter.setAttribute('href', twitter_url)
        vk.setAttribute('href', vk_url)
        ok.onclick = () => {
            window.open(ok_url, '_blank', features);
            return false
        }
        twitter.onclick = () => {
            window.open(twitter_url, '_blank', features);
            return false
        }
        vk.onclick = () => {
            window.open(vk_url, '_blank', features);
            return false
        }
    } catch { }

    /* Preloader */
    try {
        window.setTimeout(function () {
            document.body.classList.add('loaded');
            window.setTimeout(function () {
                document.getElementById('preloader').remove();
            }, 1000);
        }, 500);
    } catch { }
}


/* Header Fix */
$(function () {
    $header = $('.header');
    $window = $(window);
    $h = ($header.offset().top + 100);
    $lastHeight = 0
    $window.scroll(function () {
        if ($window.scrollTop() < 100) {
            $header.removeClass('fixed');
            $lastHeight = $window.scrollTop()
        } else if ($lastHeight > $window.scrollTop()) {
            $header.addClass('fixed');
            $lastHeight = $window.scrollTop()
        } else {
            $header.removeClass('fixed');
            $lastHeight = $window.scrollTop()
        }
    });
});

/* Back-to-top */
var offset = 200;
var duration = 500;
$(window).scroll(function () {
    if ($(this).scrollTop() > offset) {
        $('.scroll-top').fadeIn(400);
    } else {
        $('.scroll-top').fadeOut(400);
    }
    if ($(this).scrollTop() > $(document).height() - $('.footer-end').height() - $(window).height() - 100) {
        $('.scroll-top').attr('style', 'position:static;')
        $('.request-call').attr('style', 'position:static; background-color: var(--color-gray-alpha);')
        if ($(window).width() <= 500) {
            $('.footer-end__content').removeAttr('style')
            $('.scroll-top').attr('style', 'visibility:visible;')
        }
        if ($(window).width() <= 600) {
            $('.request-call').removeAttr('style')
        }
    } else {
        $('.scroll-top').removeAttr('style')
        $('.request-call').removeAttr('style')
        if ($(window).width() <= 500) {
            $('.footer-end__content').attr('style', 'position:static;')
            $('.scroll-top').attr('style', 'visibility:hidden;')
        }
        if ($(window).width() <= 600) {
            $('.request-call').attr('style', 'position:fixed !important;bottom:20px;left:20px;')
        }

    }
});
$('.scroll-top').on('click', function (event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: 0
    }, 600);
    return false;
});

/* Swiper */
const swiper = new Swiper('.swiper', {
    // Optional parameters
    loop: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    speed: 500,
    breakpoints: {
        499: {
            slidesPerView: 1,
            spaceBetween: 13
        },
        500: {
            slidesPerView: 2,
            spaceBetween: 13
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 13
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 13
        }
    }
});

/* Social-Hover-Effects */

var facebook = document.getElementsByClassName('facebook')
facebook[0].addEventListener('mouseover', () => {
    facebook[0].childNodes[1].childNodes[3].setAttribute('fill', '#1976D2')

})
facebook[0].addEventListener('mouseout', () => {
    facebook[0].childNodes[1].childNodes[3].setAttribute('fill', '#000')

})
var telegram = document.getElementsByClassName('telegram')
telegram[0].addEventListener('mouseover', () => {
    telegram[0].childNodes[1].childNodes[1].setAttribute('fill', '#1976D2')

})
telegram[0].addEventListener('mouseout', () => {
    telegram[0].childNodes[1].childNodes[1].setAttribute('fill', '#000')

})
var instagram = document.getElementsByClassName('instagram')
instagram[0].addEventListener('mouseover', () => {
    instagram[0].childNodes[1].childNodes[1].setAttribute('fill', '#BE328E')

})
instagram[0].addEventListener('mouseout', () => {
    instagram[0].childNodes[1].childNodes[1].setAttribute('fill', '#000')

})

setCurrentYear()
function setCurrentYear() {
    var year = document.getElementsByClassName('footer-end__text')[0]
    var date = new Date()
    year.getElementsByTagName('p')[0].childNodes[1].innerHTML = date.getFullYear()
}

/* Burger Menu */

try {
    burger = document.getElementById('burger')
    mobile_menu = document.getElementById('mobile-menu')
    burger.addEventListener('click', () => {
        if (mobile_menu.classList.contains('active')) {
            document.getElementsByTagName('body')[0].removeAttribute('style')
        } else {
            document.getElementsByTagName('body')[0].setAttribute('style', 'overflow:hidden;')
        }
        mobile_menu.classList.toggle('active')
    })
} catch { }


/* CALLBACK FORM Checker */

formChecker()
function formChecker() {
    formName = document.getElementById('name')
    formPhone = document.getElementById('phone')
    formInfo = document.getElementsByClassName('form__info')[0]
    formButton = document.getElementsByClassName('form__button')[0]
    lang = document.getElementById('language-code').innerHTML
    if (lang == 'ru') {
        completeAll = 'Заполните поля "Ваше имя" и "Ваш телефон"'
        completeName = 'Заполните поле "Ваше имя"'
        completePhone = 'Заполните поле "Ваш телефон"'
    } else {
        completeAll = 'The fields "Your name" and "Your phone" are empty'
        completeName = 'The field "Your name" is empty'
        completePhone = 'The field "Your phone" is empty'
    }
    formPhone.oninput = () => {
        formName.value = formName.value.trim()
        if (String(formName.value).trim() == '' && String(formPhone.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completeAll
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else if (String(formName.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completeName
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else if (String(formPhone.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completePhone
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else {
            formInfo.removeAttribute('style')
            formInfo.innerHTML = ''
            formButton.disabled = false
            formButton.removeAttribute('style')
        }
    }
    formName.oninput = () => {
        formName.value = formName.value.trim()
        if (String(formName.value).trim() == '' && String(formPhone.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completeAll
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else if (String(formName.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completeName
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else if (String(formPhone.value).trim() == '') {
            formInfo.setAttribute('style', 'display:block; color:red;')
            formInfo.innerHTML = completePhone
            formButton.disabled = true
            formButton.setAttribute('style', 'cursor:no-drop; box-shadow: none;')
        } else {
            formInfo.removeAttribute('style')
            formInfo.innerHTML = ''
            formButton.disabled = false
            formButton.removeAttribute('style')
        }
    }
}


/* Form-callback phone template */

$(function () {
    $('input[type="tel"]').mask('+99800-000-00-00');
});

/* Form Open and Close */
form_close = document.getElementsByClassName('form__close')[0]
form = document.getElementsByClassName('form')[0]
form_close.addEventListener('click', () => {
    form.classList.remove('form__active')
    document.getElementsByTagName('body')[0].removeAttribute('style')
})
function formOpen() {
    form.classList.add('form__active')
    document.getElementsByTagName('body')[0].setAttribute('style', 'overflow: hidden;')
}

/* Send CallBack to Telegram chat */

$(".form__body").submit(function (event) {
    event.preventDefault();
    lang = $("#language-code").text()
    if (lang == 'ru') {
        succesMessage = 'Сообщение успешно отправлено'
        tryAgainMessage = 'Сообщение не отправлено. Попробуйте еще раз!'
        loadingMessage = 'Загрузка...'
    } else {
        succesMessage = 'The message was sent successfully'
        tryAgainMessage = 'The message has not been sent. Try again!'
        loadingMessage = 'Loading...'
    }
    formData = $(this).serialize()
    formSendInfo = $(this).find(".form__info");
    formSendInfo.attr('style', 'display: block; color: green;')
    formSendInfo.text(loadingMessage)
    try {
        url = `http://${window.location.href.replace('http://', '').split('/')[0]}/${window.location.href.replace('http://', '').split('/')[1]}`
    } catch { url = `https://${window.location.href.replace('https://', '').split('/')[0]}/${window.location.href.replace('https://', '').split('/')[1]}` }
    $.ajax({
        url: `${url}/callback_send`,
        type: "POST",
        data: formData,
        success: function (response) {
            if (response.sended == true) {
                formSendInfo.attr('style', 'display: block; color: lime;')
                formSendInfo.text(succesMessage)
                setTimeout(() => {
                    formSendInfo.removeAttr('style')
                    formSendInfo.text('')
                }, 1000)
            }
            else {
                formSendInfo.attr('style', 'display: block; color: red;')
                formSendInfo.text(tryAgainMessage)
                setTimeout(() => {
                    formSendInfo.removeAttr('style')
                    formSendInfo.text('')
                }, 1000)
            }
        },
        error: function (response) {
            console.log(response.responseJSON)
            formSendInfo.attr('style', 'display: block; color: red;')
            formSendInfo.text(tryAgainMessage)
            setTimeout(() => {
                formSendInfo.removeAttr('style')
                formSendInfo.text('')
            }, 1000)
        }
    });
});

/* Get News */

$("#news__download").click(function (event) {
    event.preventDefault();
    $("#news__download").attr('disabled', 'True')
    $.ajax({
        url: "",
        type: "GET",
        data: { 'value': ($('.news-card').length) },
        success: function (response) {
            if (response) {
                let news__block = document.getElementsByClassName('news__block')[0]
                for (let i = 0; i < response.length; i++) {
                    article = response[i].fields
                    date = String(article.created_at).split('T')[0].split('-').reverse().join().replaceAll(',', '.')
                    let elem = document.createElement("div");
                    elem.classList.add('news-card')
                    elem.innerHTML = `
                        <div class="news-card__img">
                            <img src="/media/${article.photo}" alt="">
                        </div>
                        <div class="news-card__description">
                            <p class="news-card__type">${article.article_type}</p>
                            <p class="news-card__date"><span><img src="/static/img/news/date.svg"
                                        alt="Date"></span>${date}</p >
                            <h4 class="news-card__title">${article.title}</h4>
                            <p class="news-card__text">${article.anons}</p>
                            <a href="${article.slug}" class="news-card__button">Читать</a>
                        </div >`
                    news__block.appendChild(elem)
                }
                button = document.getElementById('news__download')
                if (parseInt(button.getAttribute('all')) <= document.getElementsByClassName('news-card').length) {
                    button.remove()
                } else {
                    button.removeAttribute('disabled')
                }
            }
        },
        error: function (response) {
            console.log(response.responseJSON)
        }
    });
});


/* Get Products */

$("#products_download").click(function (event) {
    event.preventDefault();
    $("#products_download").attr('disabled', 'True')
    $.ajax({
        url: "",
        type: "GET",
        data: { 'value': ($('.products__card').length) },
        success: function (response) {
            if (response) {
                let products__block = document.getElementsByClassName('products__block')[0]
                for (let i = 0; i < response.length; i++) {
                    product = response[i].fields
                    images = document.getElementsByClassName('products__img')
                    let imgHeight = images[0].offsetHeight
                    let elem = document.createElement("a");
                    elem.classList.add('products__card')
                    if (product.hasDescription) {
                        elem.setAttribute('href', `${product.slug}`)
                    } else {
                        elem.setAttribute('href', '#')
                    }
                    elem.innerHTML = `
                    <div class="products__img" style='height:${imgHeight}px;'>
                        <img src="/media/${product.photo}" alt="">
                    </div>
                    <div class="products__description">
                        <h3 class="products__card-title">${product.title}</h3>
                    </div>`
                    /* <p class="products__text">${product.anons}</p> */
                    products__block.appendChild(elem)
                }
                button = document.getElementById('products_download')
                if (parseInt(button.getAttribute('all')) <= document.getElementsByClassName('products__card').length) {
                    button.remove()
                } else {
                    button.removeAttribute('disabled')
                }
            }
        },
        error: function (response) {
            console.log(response.responseJSON)
        }
    });
});

/* ChangeActiveTab */

try {
    let idActiveTab = 1;

    function changeActiveTab(a) {
        document.getElementById('tab-title-' + idActiveTab).classList.remove('products-detail__tab-active');
        document.getElementById('tab-body-' + idActiveTab).classList.remove('products-detail__activeTab');
        document.getElementById('tab-title-' + a).classList.add('products-detail__tab-active');
        document.getElementById('tab-body-' + a).classList.add('products-detail__activeTab');
        idActiveTab = a;
    }
} catch { }