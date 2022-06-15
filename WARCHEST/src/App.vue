<template>
<v-app>

    <v-navigation-drawer permanent clipped v-model="drawer" app>

        <v-list dense nav>
            <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="primary" clipped-left dark src="restaurant.jpg">
        <v-toolbar-title>Site Header</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn>
            Login
        </v-btn>

    </v-app-bar>

    <v-main>
        <router-view></router-view>
    </v-main>
</v-app>
</template>

<script>
export default {
    data: () => ({
        drawer: null,
        items: [
            {
                title: 'Homepage',
                icon: 'mdi-help-box',
                to: '/homepage'
            },
            {
                title: 'App1',
                icon: 'mdi-format-list-checks',
                to: '/app1'
            },
            // {
            //     title: 'Todo',
            //     icon: 'mdi-format-list-checks',
            //     to: '/Todo'
            // },
            // {
            //     title: 'List1',
            //     icon: 'mdi-format-list-checks',
            //     to: '/list1'
            // },
        ],
    }),
}
</script>
