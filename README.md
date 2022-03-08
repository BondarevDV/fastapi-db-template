
docker-compose up -d

sudo chmod -R  777 ./data/

export GG_DATABASE_URL="postgresql://admin:admin@127.0.0.1:32700/gg_db"