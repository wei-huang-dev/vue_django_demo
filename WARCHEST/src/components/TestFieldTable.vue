<template>
<div id="app">

    <v-app id="inspire">
        <v-container>
            <v-row>
                <v-btn @click="refresh">REFRESH</v-btn>
                <v-btn @click="copy">COPY</v-btn>
            </v-row>
            <v-data-table :headers="headers" :items="items" dense disable-sort item-key="id" group-by="title">
                <template v-slot:group.header="{items, isOpen, toggle}">
                    <th colspan="20">
                        <v-icon @click="toggle">{{ isOpen ? 'mdi-minus' : 'mdi-plus' }}
                        </v-icon>
                        {{ items[0].title }}
                    </th>
                </template>
                <template v-slot:item="{ item }">
                    <tr>
                        <td v-for="(header, index) in headers">
                            <span v-if="index">{{ item.cols[index-1] }}</span>
                            <span v-else>{{ item.name }}</span>
                        </td>
                    </tr>
                </template>
            </v-data-table>

        </v-container>
    </v-app>
</div>
</template>

<script>
export default {
    data() {
        return {

            jsonData: {
                "dates": ["7/27/2022", "7/28/2022"],
                "tables": [{
                        "title": "ABC",
                        "field1": [10, 20],
                        "field2": [11, 21],
                        "field3": [12, 22],
                        "field4": [13, 23],
                        "field5": [13, 23]
                    },
                    {
                        "title": "DEF",
                        "field1": [30, 40],
                        "field2": [31, 41],
                        "field3": [32, 42],
                        "field4": [33, 43],
                        "field5": [33, 43]
                    },
                    {
                        "title": "GIJ",
                        "field1": [30, 40],
                        "field2": [31, 41],
                        "field3": [32, 42],
                        "field4": [33, 43],
                        "field5": [33, 43]
                    },
                    {
                        "title": "KLM",
                        "field1": [30, 40],
                        "field2": [31, 41],
                        "field3": [32, 42],
                        "field4": [33, 43],
                        "field5": [33, 43]
                    },
                ]
            },

            obj: null,
            responseData: null,
            index: 0,
            headers: [],
            items: [],
        }
    },
    mounted() {
        this.index = this.headers.length
    },
    methods: {
        refresh() {

            // axios.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2013-09-05').then(response => {
            //     this.responseData = response.data.bpi;

            this.responseData = this.jsonData

            this.headers = [{
                text: 'TITLE_FIELD',
            }]
            this.items = []

            // for (const $property in this.responseData) {
            //     // console.log($property)
            //     console.log(this.responseData[$property])

            //     console.log($property)
            //     console.log(this.responseData[$property])

            for (let j = 0; j < this.responseData.dates.length; j++) {
                this.headers.push({
                    text: this.responseData.dates[j],
                })
            }
            for (let i = 0; i < this.responseData.tables.length; i++) {
                this.items.push({
                    title: this.responseData.tables[i].title,
                    name: "field1",
                    cols: this.responseData.tables[i].field1
                })
                this.items.push({
                    title: this.responseData.tables[i].title,
                    name: "field2",
                    cols: this.responseData.tables[i].field2
                })
                this.items.push({
                    title: this.responseData.tables[i].title,
                    name: "field3",
                    cols: this.responseData.tables[i].field3
                })
                this.items.push({
                    //                        name: Object.keys(this.responseData.tables[i])[4],
                    title: this.responseData.tables[i].title,
                    name: "field4",
                    cols: this.responseData.tables[i].field4
                })
                this.items.push({
                    title: this.responseData.tables[i].title,
                    name: "field5",
                    cols: this.responseData.tables[i].field5
                })

            }

        },

        copy() {
            let items = this.responseData.tables
            let itemsLen = 0
            let headersLen = this.responseData.dates.length

            for (let i = 0; i < items.length; i++) {
                console.log(items[i].title)
                if (items[i].title === 'ABC') {
                    itemsLen = items[i].field1.length
                    items[i].field1.push(items[i].field1[itemsLen - 1])
                    items[i].field2.push(items[i].field2[itemsLen - 1])
                    items[i].field3.push(items[i].field3[itemsLen - 1])
                    items[i].field4.push(items[i].field4[itemsLen - 1])
                    items[i].field5.push(items[i].field5[itemsLen - 1])
                }
            }

            if (headersLen < itemsLen) {
                this.headers.push({
                    text: this.responseData.dates[headersLen - 1],
                })
            }
        }

    }
}
</script>
