<template>
<v-card hover class="my-3">
    <!-- <v-card-title class="ml-3">
        <span>{{ title }}</span>
    </v-card-title> -->
    <v-row align="center">
        <v-col cols="10">
            <div class="scrollsettings">
                <v-simple-table height="1230px" id="fieldTable">
                    <template v-slot:default>
                        <thead>
                            <tr>
                                <th class="headcol">
                                    DATE
                                </th>
                                <th class="text-left" v-for="item in dates">
                                    {{ item }}
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <template v-for="(titem, tindex) in tableTitles">
                                <tr>
                                    <td class="headcol" bgcolor=#eef>{{titem}}</td>
                                    <td  bgcolor=#eef v-for="fItem in dates">
                                    </td>
                                </tr>
                                <tr v-for="(item, index) in selectedFields.sort()">
                                    <td class="headcol" bgcolor=#efe>{{ item }}</td>
                                    <td v-for="fItem in fieldTables[tindex]">
                                        {{item.slice(-1)}}{{fItem}}
                                    </td>
                                </tr>
                            </template>
                        </tbody>
                    </template>
                </v-simple-table>
            </div>
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
            dates: [

                new Date(new Date().getTime() - 86400000).toLocaleDateString(),
                new Date().toLocaleDateString()
            ],

            tableTitles: [
                'ABC',
                'DEF',
                'GIJ',
                'KLM',
            ],

            fieldTables: [],
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
            if (this.fieldTables[x].length == this.dates.length) {
                this.newDate = new Date(this.lastDate.getTime() + 86400000); // (24 * 60 * 60 * 1000)
                this.dates.push(this.newDate.toLocaleDateString());
                this.lastDate = this.newDate;
            }
            this.fieldTables[x].push(this.fieldTables[x][this.fieldTables[x].length - 1]);
        },

        getTitle(titleIndex) {
            this.selectedCopy = titleIndex;
            this.copyLastDate(titleIndex);
        }
    },

    components: {
        'dropdownButton': require('@/components/DropdownButton.vue').default,
    }
}
</script>
