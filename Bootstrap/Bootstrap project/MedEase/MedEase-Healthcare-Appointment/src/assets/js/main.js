import "../scss/style.scss";

import * as bootstrap from "bootstrap";

import Swiper from "swiper";
import { Navigation, Pagination } from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";


// =========================
// Health Swiper
// =========================

new Swiper(".healthSwiper", {

    modules: [Navigation, Pagination],

    loop: true,

    speed: 800,

    slidesPerView: 3.15,

    spaceBetween: 30,

    centeredSlides: false,

    navigation: {
        nextEl: ".healthNext",
        prevEl: ".healthPrev",
    },

    pagination: {
        el: ".healthPagination",
        clickable: true,
    },

    breakpoints: {

        0: {
            slidesPerView: 1.1,
            spaceBetween: 16,
        },

        576: {
            slidesPerView: 1.2,
            spaceBetween: 20,
        },

        768: {
            slidesPerView: 2.2,
            spaceBetween: 24,
        },

        992: {
            slidesPerView: 3.15,
            spaceBetween: 30,
        }

    }

});


// =========================
// Testimonial Swiper
// =========================

new Swiper(".testimonialSwiper", {

    modules: [Navigation, Pagination],

    loop: false,
    speed: 600,

    slidesPerView: 1.8,
    slidesPerGroup: 1,
    spaceBetween: 24,

    navigation: {
        nextEl: ".swiper-button-next-custom",
        prevEl: ".swiper-button-prev-custom",
    },

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },


    breakpoints: {

        320: {
            slidesPerView: 1,
            spaceBetween: 16,
        },

        576: {
            slidesPerView: 1.1,
            spaceBetween: 20,
        },

        768: {
            slidesPerView: 1.3,
            spaceBetween: 20,
        },

        992: {
            slidesPerView: 1.6,
            spaceBetween: 24,
        },

        1200: {
            slidesPerView: 1.8,
            spaceBetween: 24,
        },

    },

});




new Swiper(".expertiseSwiper", {

    modules: [Navigation, Pagination],

    loop: true,

    speed: 700,

    slidesPerView: 3.15,

    spaceBetween: 24,

    navigation: {
        nextEl: ".swiper-button-next-custom",
        prevEl: ".swiper-button-prev-custom",
    },

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

    breakpoints: {

        0: {
            slidesPerView: 1.1,
            spaceBetween: 16,
        },

        576: {
            slidesPerView: 1.2,
            spaceBetween: 16,
        },

        768: {
            slidesPerView: 2.15,
            spaceBetween: 20,
        },

        992: {
            slidesPerView: 3.15,
            spaceBetween: 24,
        }

    }

});