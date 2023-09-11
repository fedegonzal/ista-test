<script setup>
import { ref, reactive, onMounted } from 'vue'
import GmapsLink from './GmapsLink.vue'
import TestHeader from './TestHeader.vue'
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
    <TestHeader 
        title="ISTA Programming Test - VueJS scratch version" 
        content="Column sorting coded from the scratch, using lodash library. Bootstrap for layout. No responsive version." 
    />

    <table id="table" class="table table-striped table-lg">
        <thead>
            <tr>
                <th @click="orderBy('id')" :class="columnOrdering.id">ID</th>
                <th @click="orderBy('university')" :class="columnOrdering.university">University</th>
                <th @click="orderBy('country')" :class="columnOrdering.country">Country</th>
                <th class="no-sort">Location</th>
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
    thead {
        position: sticky;
        top: 0;

        th {
            background-color: #036234 !important;
            color: white !important;
            cursor: pointer;

            &.asc::after {
                content: '▲';
                margin-left: .5em;
            }

            &.desc:after {
                content: '▼';
                margin-left: .5em;
            }

            &.no-sort {
                cursor: default;

                &:after {
                    content: '\01F512';
                    margin-left: .5em;
                }
            }
        }
    }

    td {
        min-width: 50px;
    }

    a {
        color: #d43900;
        text-decoration: none;
        
        &:hover {
            background-color: lightyellow;
        }
    }
}

</style>
