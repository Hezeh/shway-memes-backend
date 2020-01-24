export DATABASE_URL=berglas://${BERGLAS_BUCKET}/database_url?destination=/secrets/database_url
export SECRET_KEY=berglas://${BERGLAS_BUCKET}/secret_key?destination=/secrets/secret_key
export MEDIA_BUCKET=berglas://${BERGLAS_BUCKET}/media_bucket?destination=/secrets/media_bucket

export SUPERUSER=berglas://${BERGLAS_BUCKET}/superuser?destination=/secrets/superuser
export SUPERPASS=berglas://${BERGLAS_BUCKET}/superpass?destination=/secrets/superpass

berglas exec --local -- /bin/sh

ENVFILE=/secrets/.env

touch $ENVFILE
echo "DATABASE_URL=$(cat /secrets/database_url)" >> $ENVFILE 
echo "SECRET_KEY=$(cat /secrets/secret_key)" >> $ENVFILE 
echo "GS_BUCKET_NAME=$(cat /secrets/media_bucket)" >> $ENVFILE 

DBFILE=/secrets/database
echo "$(cat /secrets/database_url | cut -d'/' -f6)" >> $DBFILE