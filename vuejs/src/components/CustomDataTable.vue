<script setup>
import { ref, reactive, onMounted } from 'vue'
import GmapsLink from './GmapsLink.vue'

import DataTable from 'datatables.net-vue3'
import DataTablesCore from 'datatables.net'
 
const DataTableOptions = {
    fixedHeader: true, 
    paging: false, 
    searching: false
}

DataTable.use(DataTablesCore)

const props = defineProps({
    src: {
        type: String,
        required: true
    }
})


const columns = [
    { title: 'ID', data: 'id' },
    { title: 'University', data: 'university' },
    { title: 'Country', data: 'country' },
    { title: 'Location', data: 'location', render: (data, type, row) => {
        if (data !== null) {
            return `<gmaps-link :location=${JSON.stringify(data)} target="_blank" text="open location" />`
        } else {
            return 'no location'
        }
    }}
]

let institutions = ref([])

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

</script>

<template>

    <DataTable id="table" :data="institutions" :columns="columns" :options="DataTableOptions" class="stripe hover order-column row-border fixedHeader-floating">
        <thead>
            <tr>
                <th>ID</th>
                <th>University</th>
                <th>Country</th>
                <th>Location</th>
            </tr>
        </thead>

    </DataTable>
</template>

<style scoped></style>
