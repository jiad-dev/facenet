DEBUG = True

THREADS_PER_PAGE = 2

APP_NAME = 'Demo Face Embedding'

models = [
    './log/best_state.pth',
    './log/best_state_917.pth',
    './log/best_state_92.pth',
    './log/last_checkpoint.pth'
]

USE_MODEL = models[2]

SECRET_KEY = "cBWegL8d367vPzTp9Y2pJudLLtaKi5Jtw8//WsRjZrc="
