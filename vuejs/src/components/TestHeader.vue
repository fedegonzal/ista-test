<script setup>
const props = defineProps({
    title: {
        type: String,
        required: true
    },
    content: {
        type: String,
        required: true
    }
})
</script>

<template>
    <header class="row">
        <div class="col-12 col-lg-3 mb-3 mb-lg-0">
            <img class="logo" src="https://ista.ac.at/wp-content/themes/wp-theme-ist-pubwww/assets/img/logo/ISTA_Logo_4c_rgb.svg">
        </div>
        <div class="col-12 col-lg-9">
            <h1>{{ props.title }}</h1>
            <p>{{ props.content }}</p>
        </div>
    </header>
</template>

<style scoped lang="scss">
header {
    margin: 1em 0;
    .logo {
        width: 200px;
    }

    h1 {
        font-size: 2em;
    }
    p {
        font-size: 1em;
    }
}
</style>
