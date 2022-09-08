<template>
<div class="text-center">
    <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">Copy
            </v-btn>
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" @click="$emit('tableTitle', index)">
                <v-list-item-title>{{ item }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</div>
</template>

<script>
export default {
    data: () => ({
        items: [
            'ABC',
            'DEF',
            'GIJ',
            'KLM'
        ],
    }),
    methods: {
        handleClick(index) {
        },
    },
}
</script>
