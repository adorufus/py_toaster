# import sdl2.ext

# class Window:

#     __title = ''
#     __size = (0, 0)
#     __window = None

#     def __init__(self, title, size):
#         print("initializing window")
#         self.__title = title
#         self.__size = size

#     def init(self):
#         sdl2.ext.init()
        
#         self.__window = sdl2.ext.Window(self.__title, self.__size, flags=sdl2.SDL_WINDOW_RESIZABLE)
#         self.__window.show()

#     def get_window(self) -> sdl2.ext.Window:
#         return self.__window


#     def loop(self):
#         self.__window.refresh()

#     def destroy(self):
#         sdl2.ext.quit()