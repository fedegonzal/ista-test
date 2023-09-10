<script setup>
import { ref, reactive, onMounted } from 'vue'
import GmapsLink from './GmapsLink.vue'
import _ from 'lodash';

const props = defineProps({
    src: {
        type: String,
        required: true
    }
})

const institutions = ref([])

const columnOrdering = {
    'id': 'asc',
    'university': null,
    'country': null,
}

async function getData() {
    const response = await fetch(props.src);
    const data = await response.json();
    return data;
}

onMounted(() => {
    getData().then(data => {
        institutions.value = data;
    })
})

function orderBy(column) {
    let dir = columnOrdering[column] === 'asc' ? 'desc' : 'asc';

    columnOrdering.id = null;
    columnOrdering.university = null;
    columnOrdering.country = null;

    columnOrdering[column] = dir;
    institutions.value = _.orderBy(institutions.value, column, dir);
}

</script>

<template>
    <table id="table" class="stripe fixedHeader-floating">
        <thead>
            <tr>
                <th @click="orderBy('id')" :class="columnOrdering.id">ID</th>
                <th @click="orderBy('university')" :class="columnOrdering.university">University</th>
                <th @click="orderBy('country')" :class="columnOrdering.country">Country</th>
                <th>Location</th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="row in institutions" :key="row.id">
                <td>{{ row.id }}</td>
                <td>{{ row.university }}</td>
                <td>{{ row.country }}</td>
                <td v-if="row.location !== null">
                    <GmapsLink :location=row.location target="_blank" text="open location" />
                </td>
                <td v-else>no location</td>
            </tr>
        </tbody>

    </table>
</template>

<style scoped lang="scss">

table {
    min-width: 100%;

    &.stripe tr:nth-child(even) {
        background-color: rgb(249 250 251);
    }

    &.fixedHeader-floating thead {
        background-color: lightgray;
        position: sticky;
        top: 0;
    }

    th {
        text-align: initial;
        cursor: pointer;

        &.asc::after {
            content: '▲';
        }

        &.desc:after {
            content: '▼';
        }
    }

    tr {
        line-height: 2em;
    }

    th,
    td {
        padding: 5px;
    }

}
</style>
