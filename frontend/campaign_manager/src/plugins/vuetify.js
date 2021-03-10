import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        light: true,
        themes: {
            light: {
                primary: '#FF9800',
                secondary: '#9E9E9E',
                accent: '#009688',
                error: '#FF5722',
                info: '#607D8B',
                success: '#4CAF50',
                warning: '#FFC107',
            },
            dark: {
                primary: '#FF9800',
                secondary: '#9E9E9E',
                accent: '#009688',
                error: '#FF5722',
                info: '#607D8B',
                success: '#4CAF50',
                warning: '#FFC107',
            },
        },
    },
});