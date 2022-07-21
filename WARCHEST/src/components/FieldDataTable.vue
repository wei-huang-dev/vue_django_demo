<template>
<v-card hover class="my-3">
    <v-row align="center">
        <v-col cols="10">
            <v-data-table :headers="headers" :items="fieldTables" class="elevation-1">

                <template v-slot:body="props">
                    <template v-for="(titem, tindex) in tableTitles">
                        <tr>
                            <td bgcolor=#eee>{{titem}}</td>
                            <td bgcolor=#eee v-for="fItem in headers">
                            </td>
                        </tr>
                        <tr v-for="(item, index) in selectedFields">
                            <td>{{ item }}</td>
                            <td v-for="fItem in fieldTables[tindex]">
                                {{fItem}}
                            </td>
                        </tr>
                    </template>
                </template>
            </v-data-table>
        </v-col>
        <v-col class="ml-5" align="center">
            <div class="my-5"></div>
            <v-row align="center">
                <dropdownButton @tableTitle="getTitle" />
            </v-row>
            <div class="my-5"></div>
            <v-row>
                <v-btn>
                    Copy & Edit
                </v-btn>
            </v-row>
        </v-col>
    </v-row>
</v-card>
</template>

<script>
export default {
    props: {
        title: String,
        selectedFields: [],
    },
    data() {
        return {
            index: 0,
            dates: [
                new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                new Date().toLocaleDateString()
            ],
            headers: [{
                    text: 'TITLE-FIELDS',
                    align: 'start',
                    sortable: true,
                    class: 'style-1'
                },
                {
                    text: new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                    align: 'start',
                    class: 'style-1'
                },
                {
                    text: new Date().toLocaleDateString(),
                    align: 'start',
                    class: 'style-1'
                },
            ],

            fieldTables: [],

            tableTitles: [
                'ABC',
                'DEF',
                'GIJ',
                'KLM',
            ],

            lastDate: new Date(),
            newDate: new Date(),
            selectedCopy: "",
        }
    },

    mounted() {
        this.fieldTables.push([
            'xxx',
            'yyy',
        ])
        this.fieldTables.push([
            'xxx',
            'yyy',
        ])
        this.fieldTables.push([
            'xxx',
            'yyy',
        ])
        this.fieldTables.push([
            'xxx',
            'yyy',
        ])
    },
    methods: {

        copyLastDate(x) {
            // alert(this.fieldTables[x].length + "  " + this.headers.length)
            if (this.fieldTables[x].length + 1 == this.headers.length) {
                this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
                this.headers.push({
                    text: this.newDate.toLocaleDateString(),
                    class: 'style-1'

                });
                this.lastDate = this.newDate;
            }
            this.fieldTables[x].push(this.fieldTables[x][this.fieldTables[x].length - 1]);
        },

        getTitle(titleIndex) {
            // alert(titleIndex)
            this.selectedCopy = titleIndex;
            this.copyLastDate(titleIndex);

        }

    },
    components: {
        'dropdownButton': require('@/components/DropdownButton.vue').default,
    }

}
</script>
