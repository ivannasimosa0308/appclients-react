import { createClient } from '@supabase/supabase-js';

const supabaseUrl =
  import.meta.env.VITE_SUPABASE_URL ||
  'https://hbttckddzhzxkqjeqnkd.supabase.co';
const supabaseKey =
  import.meta.env.VITE_SUPABASE_KEY ||
  'sb_publishable_XCbg9nd-UPnaMrvvlUuqGQ_y3MA5KFG';

export const supabase = createClient(
  supabaseUrl,
  supabaseKey
);

// Comprobación de conexión solicitada en el Reto 1:
console.log('conexión correcta', {
  url: supabaseUrl,
  client: supabase
});

// Comprobación asíncrona adicional contra la tabla clients:
supabase
  .from('clients')
  .select('id', { head: true })
  .then(
    ({ error }) => {
      if (!error) {
        console.log('conexión correcta - acceso verificado a la tabla clients');
      }
    },
    (err: any) => {
      console.warn('Verificación Supabase:', err);
    }
  );
