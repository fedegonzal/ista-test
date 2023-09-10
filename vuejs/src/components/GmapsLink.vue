<script setup>
import { ref, reactive } from 'vue'

defineProps({
    location: {
        type: Object,
        required: true
    },
    target: {
        type: String,
        required: true
    },
    text: {
        type: String,
        required: true
    },
})
</script>

<template>
    <a 
        :href="'https://www.google.com/maps?q=' + location.lat + ',' + location.lng" 
        target="{{ target }}">
        {{ text }}
    </a>
</template>

<style scoped></style>
