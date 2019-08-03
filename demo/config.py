DEBUG = True

THREADS_PER_PAGE = 2

APP_NAME = 'Demo Face Embedding'

models = [
    './log/best_state.pth',
    './log/best_state_917.pth',
    './log/model921-af60fb4f.pth',
    './log/model920-6be7e3e9.pth'
]

USE_MODEL = models[2]

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="
