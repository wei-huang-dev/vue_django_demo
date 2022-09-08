<style>
@import '../assets/app.css';
</style>

<template>
<v-container fluid>

    <v-expansion-panels focusable>
        <v-expansion-panel>
            <v-expansion-panel-header>Filters</v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row>
                    <v-col class="ml-10">
                        <v-combobox v-model="state" :items="states" label="State" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="county" :items="counties" label="County" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="town" :items="towns" label="Town" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="model" :items="models" label="Model" multiple outlined dense></v-combobox>
                    </v-col>
                    <v-col class="mr-10">
                        <v-combobox v-model="color" :items="colors" label="Color" multiple outlined dense></v-combobox>
                    </v-col>
                </v-row>
            </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
            <v-expansion-panel-header>Group By</v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row>
                    <v-col class="ml-10">
                        <v-checkbox v-model="stateX" :label="`State`"></v-checkbox>
                    </v-col>
                    <v-col>
                        <v-checkbox v-model="countyX" :label="`County`"></v-checkbox>
                    </v-col>
                    <v-col>
                        <v-checkbox v-model="townX" :label="`Town`"></v-checkbox>
                    </v-col>
                </v-row>
            </v-expansion-panel-content>
        </v-expansion-panel>

    </v-expansion-panels>

    <fieldSimpleTable />
    <!-- <jsonFieldTable />

    <fluidTable /> -->

</v-container>
</template>

<script>
export default {
    data() {
        return {
            id: 0,
            checkedNames: [],
            stateX: true,
            countyX: false,
            townX: false,
            state: [],
            states: [
                'State 1',
                'State 2',
                'State 31',
                'State 42',
                'State 51',
                'State 62',
                'State 71',
                'State 82',
                'State 91',
                'State 14',
                'State 21',
                'State 31',
                'State 26',
                'State 18',
                'State 26',
                'State 19',
            ],
            county: [],
            counties: [
                'county 1',
                'county 2',
            ],
            town: [],
            towns: [
                'town 1',
                'town 2',
            ],
            model: [],
            models: [
                'model 1',
                'model 2',
            ],
            color: [],
            colors: [
                'color 1',
                'color 2',
            ],
        }
    },
    methods: {},
    components: {
        'fieldSimpleTable': require('@/components/FieldSimpleTable.vue').default,
        // 'jsonFieldTable': require('@/components/JsonFieldTable.vue').default,
        // 'fluidTable': require('@/components/FluidTable.vue').default,
    }
}
</script>
