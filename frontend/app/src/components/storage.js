import { join } from 'path'
import { get } from 'lodash'
import { Storage } from '@google-cloud/storage'


const gcloudPathKey = require('../gcpkey.json')

const storage = new Storage({
  projectId: 'hacking-348118',
  keyFilename: gcloudPathKey
})

export const uploadAndGetPublicFile = async (
  fileName,
  data,
  defaultMimeType
) => {

  const [bucketExist] = await storage
  .bucket('hackerbucket')
  .exists();
  if (!bucketExist) {
    await storage.createBucket('hackerbucket');
  }

  const file = storage
  .bucket('hackerbucket')
  .file(fileName);

  const fileOptions = {
    public: true,
    resumable: false,
    metadata: { contentType: 'image/jpeg' },
    validation: false
  }
  if (typeof data === 'string') {
    const base64EncodedString = data.replace(/^data:\w+\/\w+;base64,/, '')
    const fileBuffer = Buffer.from(base64EncodedString, 'base64')
    await file.save(fileBuffer, fileOptions);
  } else {
    await file.save(get(data, 'buffer', data), fileOptions);
  }
  const publicUrl = `https://storage.googleapis.com/hackerbucket/${fileName}`

  const [metadata] = await file.getMetadata()
  return {
    ...metadata,
    publicUrl
  }
}

export default storage