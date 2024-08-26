from fastapi import HTTPException, status

class NoteException(HTTPException):
    status_code = 500
    detail = ""
    
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class IncorrectEmailOrPasswordException(NoteException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"

class UserAlreadyExistsException(NoteException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"
             
class TokenExpiredException(NoteException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"
        
class TokenAbsentException(NoteException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"
        
class IncorrectTokenFormatException(NoteException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"
        
class UserIsNotPresentException(NoteException):
    status_code=status.HTTP_401_UNAUTHORIZED