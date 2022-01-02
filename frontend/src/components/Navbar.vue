<template>
  <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto px-2 sm:px-4 lg:pl-6">
      <div class="relative flex items-center justify-between h-16">
        <div class="absolute inset-y-0 left-0 flex items-center md:hidden">
          <!-- Mobile menu button-->
          <DisclosureButton
            class="
              inline-flex
              items-center
              justify-center
              p-2
              rounded-md
              text-gray-400
              hover:text-white hover:bg-gray-700
              focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white
            "
          >
            <span class="sr-only">Open main menu</span>
            <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div
          class="
            flex-1 flex
            items-center
            justify-center
            md:items-stretch md:justify-start
          "
        >
          <div class="flex-shrink-0 flex items-center">
            <img
              class="block lg:hidden h-8 w-auto"
              src="https://tailwindui.com/img/logos/workflow-mark-indigo-500.svg"
              alt="Workflow"
            />
            <img
              class="hidden lg:block h-8 w-auto"
              src="https://tailwindui.com/img/logos/workflow-logo-indigo-500-mark-white-text.svg"
              alt="Workflow"
            />
          </div>
          <div class="hidden md:block sm:ml-6">
            <div class="flex space-x-4">
              <router-link
                v-for="(item, key) in this.navigation"
                :to="item.destination"
                @click="handleCurrent(item)"
                :key="key"
                :class="[
                  'px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-900',
                  item.current
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white',
                ]"
                :aria-current="item.current ? 'page' : undefined"
              >
                {{ item.name }}
              </router-link>
            </div>
          </div>
        </div>
        <searchbar />
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <DisclosureButton
          v-for="(item, key) in this.navigation"
          :key="key"
          @click="handleCurrent(item)"
          :to="item.destination"
          :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-gray-300 hover:bg-gray-900 hover:text-white',
            'block px-3 py-2 rounded-md text-base font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
        >
          {{ item.name }}
        </DisclosureButton>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>

<script>
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from '@headlessui/vue'
import { BellIcon, MenuIcon, XIcon } from '@heroicons/vue/outline'

export default {
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
    BellIcon,
    MenuIcon,
    XIcon,
  },
  data() {
    return {
      navigation: [
        {
          name: 'Gallery',
          destination: {
            name: 'PaintingList',
            params: { url: '/painting/all' },
          },
          current: false,
        },
        {
          name: 'Artists',
          destination: {
            name: 'CreatorList',
            params: { url: '/creator/all' },
          },
          current: false,
        },
        {
          name: 'Depicts',
          destination: {
            name: 'DepictionList',
            params: { url: '/depiction/all' },
          },
          current: false,
        },
        {
          name: 'Movements',
          destination: {
            name: 'MovementList',
            params: { url: '/movement/all' },
          },
          current: false,
        },
        {
          name: 'Materials',
          destination: {
            name: 'MaterialList',
            params: { url: '/material/all' },
          },
          current: false,
        },
      ],
    }
  },
  methods: {
    handleCurrent(clickedItem) {
      this.navigation.forEach((item) => {
        item.current = false
      })

      clickedItem.current = true
    },
  },
}
</script>
