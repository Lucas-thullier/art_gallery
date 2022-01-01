<template>
  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
      <div
        class="
          flex
          items-end
          justify-center
          min-h-screen
          pt-4
          px-4
          pb-20
          text-center
          sm:block sm:p-0
        "
      >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <DialogOverlay
            class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
            @click="this.$emit('setModal', false)"
          />
        </TransitionChild>

        <!-- This element is to trick the browser into centering the modal contents. -->
        <span
          class="hidden sm:inline-block sm:align-middle sm:h-screen"
          aria-hidden="true"
          >&#8203;</span
        >
        <TransitionChild
          as="template"
          enter="ease-out duration-300"
          enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          enter-to="opacity-100 translate-y-0 sm:scale-100"
          leave="ease-in duration-200"
          leave-from="opacity-100 translate-y-0 sm:scale-100"
          leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        >
          <div
            class="
              inline-block
              align-bottom
              bg-gray-700
              rounded-lg
              text-left
              overflow-hidden
              shadow-xl
              transform
              transition-all
              sm:align-middle sm:max-h-screen
            "
          >
            <button
              type="button"
              class="
                mt-3
                absolute
                text-base
                font-medium
                text-white
                top-0
                right-2
                p-3
              "
              @click="this.$emit('setModal', false)"
              ref="cancelButtonRef"
            >
              <XIcon class="w-10 transition ease-in-out hover:text-zinc-500" />
            </button>
            <img
              class="rounded object-scale-down max-h-screen"
              :src="picture"
            />
          </div>
        </TransitionChild>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script>
import { ref } from 'vue'
import {
  Dialog,
  DialogOverlay,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue'
import { ExclamationIcon, XIcon } from '@heroicons/vue/outline'

export default {
  props: {
    picture: String,
    open: Boolean,
  },
  components: {
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
    ExclamationIcon,
    XIcon,
  },
}
</script>
