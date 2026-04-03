@echo off
echo ========================================
echo  MarcenAI - Reiniciar Sistema
echo ========================================
echo.
echo Parando containers...
docker-compose down
echo.
echo Removendo volumes antigos...
docker-compose down -v
echo.
echo Iniciando novamente...
docker-compose up --build
