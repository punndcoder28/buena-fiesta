const colors = require('tailwindcss/colors');

const content = (process.env.TAILWIND_CONTENT_PATH || '').split(/:/);

module.exports = {
    content,
    theme: {
        extend: {
            colors: {
                primary: colors.rose['500'],
            },
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms')({
            strategy: 'class',
        }),
        // remove?
        require('flowbite/plugin'),
        require('daisyui'),
    ],
    daisyui: {
        themes: [
            {
                fiesta: {
                    "primary": "#f43f5e",
                    "secondary": "#7b3ff4",
                    "accent": "#FFBC0A",
                    "neutral": "#3D4451",
                    "base-100": "#FFFFFF",
                    "info": "#A6E1FA",
                    "success": "#69DC9E",
                    "warning": "#FBBD23",
                    "error": "#F87272",
                },
            },
        ],
    },
};
